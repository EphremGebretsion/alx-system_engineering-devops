# this is a puppet script that configures nginx
package { 'Nginx':
ensure   => installed,
name     => 'nginx',
provider => 'apt',
}
file { 'tes':
ensure  => present,
path    => '/tmp/tes',
content => 'Hello World!',
}
file_line { 'root':
ensure => present,
path   => '/etc/nginx/sites-available/default',
line   => 'root /tmp;',
match  => 'root .*;',
}
exec { 'sites-enabled':
command => '/usr/bin/ln -f -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default',
}
exec { 'index':
command => '/usr/bin/sed -i 's/index /index tes /' /etc/nginx/sites-available/default',
}
exec { 'redirect':
command => ''/usr/bin/sed -i 's|server_name _;|server_name _;\n\nlocation /redirect_me \
{\n\t\treturn 301 https:\/\/www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\
|' /etc/nginx/sites-available/default'',
}
