# Create a manifest that kills a process named killmenow.

exec { 'pKill':
  command => 'pkill killmenow',
  provide => 'shell',
}
