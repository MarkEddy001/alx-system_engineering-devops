# a manifest that kills a process named killmenow.

# Requirements:

# Must use the exec Puppet resource
# Must use pkill

exec {
    'pkill':
    command => '/usr/bin/pkill killmenow',
}
