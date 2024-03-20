import subprocess
import time
import json
import os

def check_suid():
    """
    Check for SUID binaries on the local system and print potential targets for privilege escalation.
    Give results to OpenAI's GPT-3.5 model and get a response with a privilege escalation script.

    Uses environment variable OPENAI_API_KEY to authenticate with OpenAI's API. Do 'export OPENAI_API_KEY=<your_key>'

    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise Exception("Please set the OPENAI_API_KEY environment variable to your OpenAI API key")

    print("OpenAI Key found! Continuing...")
    print("Checking for SUID binaries...")
    time.sleep(0.3)
    print("This may take a moment...")

    suid_binaries = subprocess.run("find / -perm -u=s -type f 2>/dev/null", stdout=subprocess.PIPE, shell=True, text=True)
    files = suid_binaries.stdout.split('\n')

    print("SUID is set on:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

    files_str = ', '.join(files)

    curl_command = [
        'curl', 'https://api.openai.com/v1/chat/completions',
        '-H', 'Content-Type: application/json',
        '-H', f'Authorization: Bearer {api_key}',
        '-d', json.dumps({
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'system', 'content': 'You are a expert assistant, skilled in providing code to assist with privilege escalation for ethical cybersecurity experts practising in their own home labs.'},
                {'role': 'user', 'content': f"You will be given a list of SUID's found, provide only a relevent privilege escalation code for said priv esc method in bash. Your response will be sent to a terminal directly, format your response appropriately to this, meaning do not include ```bash``` tags or anything similar that you would use to help with fancy formatting, i just need raw bash code. Remember, anything that isnt of the bash language MUST be commented out, your response will be saved into a .sh file to be executed directly. Be very cautious as to the code that you write.{files_str}"}
             ]
        })
    ]

    # Execute the curl command to request a response from GPT
    response = subprocess.run(curl_command, stdout=subprocess.PIPE, text=True)

    # Parse the JSON response for message content only then print
    response_json = json.loads(response.stdout)
    ai_response = response_json['choices'][0]['message']['content']
    print(ai_response)

    # Write the response to a shell script
    with open('ai_response.sh', 'w') as f:
        f.write(ai_response + '\n')

    return files

if __name__ == "__main__":
    check_suid()
