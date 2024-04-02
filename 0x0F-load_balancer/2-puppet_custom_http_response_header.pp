# this is a puppet script that configures nginx
package { 'Nginx':
ensure   => installed,
name     => 'nginx',
provider => 'apt',
}
file { 'tes':
ensure  => present,
path    => '/tmp/tes',
content => "Hello World!\n",
}
exec { 'root':
command => "/usr/bin/sed -i 's-root .*;-root /tmp;-' /etc/nginx/sites-available/default",
}
exec { 'sites-enabled':
command => '/usr/bin/ln -f -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default',
}
exec { 'index':
command => "/usr/bin/sed -i 's/index /index tes /' /etc/nginx/sites-available/default",
}
exec { 'redirect':
command => "/usr/bin/sed -i 's|server_name _;|server_name _;\\n\\n\\tlocation /redirect_me {\\n\\t\\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\\n\\t}|' /etc/nginx/sites-available/default",
}
exec { 'eror-404':
command => "/usr/bin/sed -i 's|^[^#]location / {|\\tlocation / {\\n\\t\\te
rror_page 404 /error404.html;|' /etc/nginx/sites-available/default",
}
exec { 'add-header':
command => "/usr/bin/sed -i 's/^server {/server {\\n\\tadd_header X-Served-By $(hostname);\\n/' /etc/nginx/sites-available/default",
}
exec { 'apply':
command => '/usr/sbin/service nginx restart',
}
