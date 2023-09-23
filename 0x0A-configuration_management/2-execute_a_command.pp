# Create a manifest that kills a process named killmenow.

exec { 'Kill_process':
  command  => 'pkill killmenow',
  provider => 'shell',
}
