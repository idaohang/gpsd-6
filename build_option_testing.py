
import os

always_on = [
    'minimal',
]

always_off = [
    'leapfetch',
]

other = [
    'debug',
    'chrpath',
    'ipv6',
    'manbuild',
    'nostrip',
    'slow',
    'profiling',
    'libQgpsmm',
]

knobs = [
    'reconfigure',
    'aivdm',
    'ashtech',
    'bluez',
    'clientdebug',
    'control_socket',
    'controlsend',
    'coveraging',
    'dbus_export',
    'earthmate',
    'evermore',
    'force_global',
    'fury',
    'fv18',
    'garmin',
    'garmintxt',
    'geostar',
    'gpsclock',
    'itrax',
    'libgpsmm',
    'mtk3301',
    'navcom',
    'ncurses',
    'netfeed',
    'nmea0183',
    'nmea2000',
    'nofloats',
    'ntpshm',
    'ntrip',
    'oceanserver',
    'oldstyle',
    'oncore',
    'passthrough',
    'pps',
    'python',
    'qt',
    'rtcm104v2',
    'rtcm104v3',
    'shared',
    'shm_export',
    'sirf',
    'socket_export',
    'squelch',
    'superstar2',
    'systemd',
    'timing',
    'tnt',
    'tripmate',
    'tsip',
    'ublox',
    'usb',
]

import itertools
failed_configurations = []

for i in range(0, len(knobs)):
    jj = itertools.combinations(knobs, i)

    for row in list(jj):
        params = []

        for key in always_on:
            params.append(key+"=on")

        for key in always_off:
            params.append(key+"=off")

        for key in knobs:
            if key in row:
                params.append(key+"=on")

        #print {'on_params': row, 'scons_params': params}

        import subprocess
        command = ['scons', '-j9']
        command.extend(params)
        if os.path.exists('.scons-option-cache'):
            os.remove('.scons-option-cache')

        retval = subprocess.call(command)
        if retval != 0:
            failed_configurations.append(command)
            print command
            with open('failed_build_configs.txt', 'a') as failed_configs:
                failed_configs.write(' '.join(command) + '\n')

for row in failed_configurations:
    print ' '.join(row)
