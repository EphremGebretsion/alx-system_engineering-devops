# installing flask 2.1.0 using pip3
package { 'Flask':
ensure   => '2.1.0',
name     => 'flask',
provider => 'pip3',
require  => Package['Werkzeg'],
}
package { 'Werkzeg':
ensure   => '2.1.1',
name     => 'werkzeug',
provider => 'pip3',
}
