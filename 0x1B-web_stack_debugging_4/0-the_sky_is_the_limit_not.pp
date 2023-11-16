# requests to server
exec { 'change':
  provider => shell,
  command  => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  before   => Exec['restart'],
}

exec { 'restart':
  provider => shell,
  command  => 'service nginx restart',
}
