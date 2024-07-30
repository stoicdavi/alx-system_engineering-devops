# Manifest that kills a process named killmenow
# uses exec resource with pkill command

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
