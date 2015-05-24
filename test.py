import meshblu
import json

def main():
    m = meshblu.MeshbluRestClient()
    s = m.getStatus()
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":
    main()
