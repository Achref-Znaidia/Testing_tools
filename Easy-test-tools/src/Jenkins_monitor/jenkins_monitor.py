import jenkins

server = jenkins.Jenkins(jenkins_url, username=username, password=api_token)
user = server.get_whoami()
version = server.get_version()
print(f"Hello {user['fullName']} from Jenkins {version}")
