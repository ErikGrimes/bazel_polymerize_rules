import sys, subprocess, os

BASE_DIR = "${base_dir}"
OVERRIDES = "${overrides}"
PUB_HOSTED_URL = "${pub_host}"
CACHE_DIR = "${cache_dir}"
DART_HOME="${dart_home}"


def pub(pkg_name, pkg_version):
    if (not os.path.exists(BASE_DIR)):
        os.makedirs(BASE_DIR)
    pubspec = open(os.path.join(BASE_DIR, "pubspec.yaml"),mode='w')
    pubspec.write("""
# MADE BY Polymerizy - PY
name: %s_pub
dependencies:
 %s: "%s"
""" % (pkg_name, pkg_name, pkg_version))

    pubspec.close()

    #with open(os.path.join(BASE_DIR, ".publog"),mode='w') as log :

    if OVERRIDES:
         SOURCE_ARGS = ['--source', 'path', OVERRIDES]
    else:
         SOURCE_ARGS = [pkg_name, pkg_version]

    proc = subprocess.Popen(['%s/pub' % (DART_HOME), 'global', 'activate'] + SOURCE_ARGS, env={
         'PUB_HOSTED_URL': PUB_HOSTED_URL,
         'PUB_CACHE': CACHE_DIR,
         'HOME':BASE_DIR
    })

    proc.wait()

    #if (proc.returncode!=0) :
    #    print("COULD NOT INITIALIZE POLYMERIZE FOR BAZEL !!!! Please retry with a bazel clean");
    return proc.returncode


if __name__ == '__main__':
    exit(pub(sys.argv[1], sys.argv[2]))
