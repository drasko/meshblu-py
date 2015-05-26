import meshblu
import json

def main():
    m = meshblu.MeshbluRestClient('http://meshblu.octoblu.com')

    print "# getStatus()"
    s = m.getStatus()
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# addDevice()"
    #s = m.addDevice({'type':'user', 'id':'drasko'})
    #print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    # "uuid":"86c6e9d1-b8a6-42e2-b411-aaecbaaaa969","token":"578e4904a4c42402a16dd409672c8da7218ecf5c"
    m.setCredentials("86c6e9d1-b8a6-42e2-b411-aaecbaaaa969", "578e4904a4c42402a16dd409672c8da7218ecf5c")

    print "# addDevices()"
    s = m.getDevices({'id':'drasko'})
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    s = m.getDevice("86c6e9d1-b8a6-42e2-b411-aaecbaaaa969")
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":
    main()
