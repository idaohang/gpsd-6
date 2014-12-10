
knobs = [
    'nmea0183',
    'ashtech',
    'earthmate',
    'evermore',
    'fv18',
    'garmin',
    'garmintxt',
    'geostar',
    'itrax',
    'mtk3301',
    'navcom',
    'oncore',
    'sirf',
    'superstar2',
    'tnt',
    'tripmate',
    'tsip',
    'ublox',
    'fury',
    'nmea2000',
    'aivdm',
    'gpsclock',
    'ntrip',
    'oceanserver',
    'rtcm104v2',
    'rtcm104v3',
]

import itertools
failed_configurations = []

for i in range(0, len(knobs)):
    jj = itertools.combinations(knobs, i)

    for row in list(jj):
        params = []
        for key in knobs:
            if key in row:
                params.append(key+"=on")
            else:
                params.append(key+"=off")
        #print {'on_params': row, 'scons_params': params}

        import subprocess
        command = ['scons', 'testregress']
        command.extend(params)
        retval = subprocess.call(command)
        if retval != 0:
            failed_configurations.append(command)
            print command
            with open('failed_build_configs.txt', 'a') as failed_configs:
                failed_configs.write(' '.join(command) + '\n')

for row in failed_configurations:
    print ' '.join(row)
