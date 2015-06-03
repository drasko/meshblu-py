import meshblu
import json


def main():
    m = meshblu.MeshbluRestClient('http://meshblu.octoblu.com')

    print "# getStatus()"
    s = m.getStatus()
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "==="

    print "# CREATE USER"
    user = m.addDevice({'type':'device', 'id':'weio'})
    print json.dumps(user, sort_keys=True, indent=4, separators=(',', ': '))

    print "# addDevice()"
    dev = m.addDevice({'type':'device', 'id':'weio'})
    print json.dumps(dev, sort_keys=True, indent=4, separators=(',', ': '))

    print "# setCredentials()"
    m.setCredentials(user['uuid'], user['token'])

    print "# addDevices()"
    s = m.getDevices({'id':'drasko'})
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    s = m.getDevice(user['uuid'])
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getDeviceToken()"
    s = m.getDeviceToken(user['uuid'])
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getLocalDevices()"
    s = m.getLocalDevices()
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# claimDevice()"
    s = m.claimDevice(dev['uuid'])
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getMyDevices()"
    s = m.getMyDevices()
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# updateDevice()"
    s = m.updateDevice(dev['uuid'], {'id':'WeIO2'})
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getMyDevices()"
    s = m.getMyDevices()
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# deleteDevice()"
    #s = m.deleteDevice(dev['uuid'])
    #print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getMyDevices()"
    s = m.getMyDevices()
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "==="

    print "# sendMessage()"
    print "Sending message to: ", dev['uuid']
    print "meshblu_auth_uuid: ", user['uuid'], " meshblu_auth_token: ", user['token']
    s = m.sendMessage({"devices": dev['uuid'], "payload": {"yellow":"off"}})
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    #print "# whoami()"
    #s = m.whoami()
    #print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getIpAddr()"
    s = m.getIpAddr()
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))


    #print "\n", dev['uuid'], "\n"
    #print "# getEvents()"
    #s = m.getEvents(dev['uuid'])
    #print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    #print "\n", dev['uuid'], "\n"
    #print "# subscribe()"
    #print user['uuid'], user['token']

    print "curl -X POST -H \"Content-Type: application/json\" -d '{\"devices\": \"" + "*" + "\", \
\"payload\": {\"yellow\":\"off\"}}' https://meshblu.octoblu.com/messages --header \
\"meshblu_auth_uuid: " + dev['uuid'] + "\" --header \"meshblu_auth_token: " + dev['token'] + "\""
    s = m.subscribeUuidBroadcast(dev['uuid'])
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# setData()"
    s = m.setData(dev['uuid'], {'wind':'78', 'temp':'100'})
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getData()"
    s = m.getData(dev['uuid'])
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# setData()"
    s = m.setData(dev['uuid'], {'wind':'55', 'temp':'66'})
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getData()"
    s = m.getData(dev['uuid'])
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getData()"
    print "USER: ", user['uuid'], "   ", user['token']
    print "DEVICE: ", dev['uuid']

    print "curl -X POST -d \"wind=12&temperature=78\" https://meshblu.octoblu.com/data/" + dev['uuid'] + " --header \"meshblu_auth_uuid: " + user['uuid'] + "\" \
--header \"meshblu_auth_token: " + user['token'] + "\""
    s = m.getData(dev['uuid'], True)
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))



if __name__ == "__main__":
    main()
