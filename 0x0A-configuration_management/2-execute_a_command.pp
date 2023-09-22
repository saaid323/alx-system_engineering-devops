# Create a manifest that kills a process named killmenow.

exec { 'Kill_now':
  command => 'pkill killmenow',
  provide => 'shell',
}
