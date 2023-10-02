#  automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update':
  command  => 'sudo apt-get -y update',
  path     => '/usr/bin',
  logoutput => true,
  require  => Package['nginx'],
  before   => Exec['install_nginx'],
}

package { 'nginx':
  ensure  => 'installed',
}

exec { 'install_nginx':
  command  => 'sudo apt-get -y install nginx',
  path     => '/usr/bin',
  logoutput => true,
  before   => Exec['add_header'],
}

exec { 'add_header':
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  path        => '/usr/bin',
  logoutput   => true,
  notify      => Exec['restart_nginx'],
  require     => Package['nginx'],
}

exec { 'restart_nginx':
  command  => 'sudo service nginx restart',
  path     => '/usr/bin',
  logoutput => true,
  refreshonly => true,
}

