import meshblu
import json


def testStatus():
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
    s = m.sendMessage({"devices": dev['uuid'], "payload": {"yellow":"off"}})
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))

    print "# getEvents()"
    s = m.getEvents(dev['uuid'])
    print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))



if __name__ == "__main__":
    testStatus()
    #testDevices()
    testMessages()
