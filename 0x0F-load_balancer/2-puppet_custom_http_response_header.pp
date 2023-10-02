#  automate the task of creating a custom HTTP header response, but with Puppet.
exec { 'update':
  command     => 'apt-get -y update',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}
exec { 'apt-get':
  command => 'apt-get -y install nginx',
  path    => '/usr/bin:/bin',
  require => Exec['update'],
}

-> file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'redirect':
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'server_name _;',
  line   => "\tlocation /redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}",
  notify => Exec['restart'],
}

file_line { 'add_header':
  path   => '/etc/nginx/sites-enabled/default',
  after  => "^\tlocation / {",
  line   => "\t\tadd_header X-Served-By \"${::hostname}\";",
  notify => Exec['restart'],
}

exec { 'restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File_line['redirect'],
}
