# Using Puppet, install flask from pip3.

# Requirements:

# Install flask
# Version must be 2.1.0

package {
    'python3.8':
    ensure  => '3.8.10',
}

package {
    'python3-pip':
    ensure  => installed,
}

package {
    'flask':
    ensure   => '2.1.0',
    require  => Package['python3-pip'],
    provider => 'pip',
}

package {
    'Werkzeug':
    ensure   => '2.1.0',
    require  => Package['python3-pip'],
    provider => 'pip',
}
