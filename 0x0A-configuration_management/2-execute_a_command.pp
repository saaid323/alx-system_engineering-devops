# Create a manifest that kills a process named killmenow.

exec { "Kill_process":
  command => 'pkill 9 killmenow',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  onlyif  => 'pgrep killmenow',
}
