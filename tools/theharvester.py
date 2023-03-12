import subprocess

def run_theharvester(domain, navigator):
    cmd = ['theHarvester', '-d', domain, '-l', '200', '-b', navigator]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':

    output = run_theharvester(domain, navigator)
    print(output)
