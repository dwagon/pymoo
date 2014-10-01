#!/usr/bin/env python

import requests
import sys

server = 'http://localhost:8000/api/v1'


###############################################################################
def getStuff(url):
    r = requests.get('%s/%s' % (server, url))
    return r.json()


###############################################################################
def getGame(gamenum=1):
    r = getStuff('game/%d' % gamenum)
    return r


###############################################################################
def getSystem(sysnum):
    r = getStuff('system/%d' % sysnum)
    return r


###############################################################################
def getPlanet(plannum):
    r = getStuff('planet/%d' % plannum)
    return r


###############################################################################
def planetDetail(sysn):
    planets = {}
    for plannum in sysn['planets']:
        p = getPlanet(plannum)
        planets[p['orbit']] = p
    ans = []
    for p in sorted(planets.keys()):
        ans.append(planets[p]['name'])
    return ", ".join(ans)


###############################################################################
def main():
    game = getGame()
    systems = {}
    for snum in game['systems']:
        syst = getSystem(snum)
        systems[(syst['x'], syst['y'])] = syst

    sys.stdout.write('    ' + '-' * game['max_x'] + '\n')
    lasts = None
    for y in range(game['max_y']):
        sys.stdout.write("%02d |" % y)
        for x in range(game['max_x']):
            if (x, y) in systems:
                sys.stdout.write('X')
                lasts = systems[(x, y)]
            else:
                sys.stdout.write(' ')
        if lasts:
            sys.stdout.write(" - %s: %s" % (lasts['name'], planetDetail(lasts)))
            lasts = None
        sys.stdout.write('\n')


###############################################################################
if __name__ == "__main__":
    main()

# EOF
