#  automate the task of creating a custom HTTP header response, but with Puppet.
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install'],
}

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['header'],
}

exec { 'header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart'],
}

exec { 'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
