[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=300&size=34&pause=1000&random=false&width=852&lines=Sticky+-+AI+Powered+Privilege+Escalation)](https://git.io/typing-svg)

This Python script is designed to check for SUID binaries on the local system and provide potential targets for privilege escalation. It utilizes OpenAI's GPT-3.5 model to generate a privilege escalation script based on the SUID binaries found.
<h2>Usage</h2>

  Ensure you have set up an OpenAI API key and exported it as the OPENAI_API_KEY environment variable.
  Run the script by executing `python sticky.py`

<h2>Requirements</h2>

  - Python
  - OpenAI API Key

<h2>Setup</h2>

  Clone this repository to your local machine.
  
  Set up your OpenAI API key by exporting it as an environment variable:
    
    export OPENAI_API_KEY=<your_api_key>

<h2>Script Explanation</h2>

  The script utilizes the subprocess module to execute shell commands for finding SUID binaries and making API requests to OpenAI.
  It checks for the presence of the OPENAI_API_KEY environment variable and raises an exception if it's not set.
  
  SUID binaries are searched using the find command, specifically `find / -perm -u=s -type f 2>/dev/null`.
  The list of SUID binaries found is passed as input to OpenAI's GPT-3.5 model to generate a privilege escalation script based on the findings.
  The generated script is saved to a .sh file for execution.

<h2>Disclaimer</h2>

  This script is intended for educational purposes and ethical hacking activities only.
  Use it responsibly and with proper authorization.
  Be cautious when executing scripts generated by AI models, as they may cause unintended consequences.

<h2>Contributing</h2>

Contributions are welcome! Feel free to open an issue or submit a pull request.
