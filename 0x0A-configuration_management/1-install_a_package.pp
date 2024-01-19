# Install a specific version of flask (2.1.0)
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 freeze | /bin/grep Flask | /bin/grep 2.1.0',
}
