<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'freeswitch';
$app['version'] = '1.0.0';
$app['release'] = '1';
$app['vendor'] = 'WikiSuite';
$app['packager'] = 'eGloo';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('freeswitch_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('freeswitch_app_name');
$app['category'] = lang('base_category_server');
$app['subcategory'] = lang('base_subcategory_communication_and_collaboration');

/////////////////////////////////////////////////////////////////////////////
// Controllers
/////////////////////////////////////////////////////////////////////////////

$app['controllers']['freeswitch']['title'] = $app['name'];
$app['controllers']['settings']['title'] = lang('base_settings');

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['core_requires'] = array(
    'app-users-core >= 1:2.3.23',
    'app-groups-core',
    'app-network-core',
    'freeswitch-config-vanilla',
    'freeswitch-lang-de',
    'freeswitch-lang-es',
    'freeswitch-lang-fr',
    'freeswitch-lang-he',
    'freeswitch-lang-pt',
    'freeswitch-lang-ru',
    'freeswitch-lang-sv',
    'freeswitch-sounds-music',
    'freeswitch-sounds-en-ca-june-all',
    'freeswitch-sounds-en-us-callie-all',
    'freeswitch-sounds-fr-ca-june-all',
    'freeswitch-sounds-ru-RU-elena-all',
);

$app['core_directory_manifest'] = array(
    '/var/clearos/freeswitch' => array(),
    '/var/clearos/freeswitch/backup' => array(),
);

$app['core_file_manifest'] = array(
    'freeswitch.php'=> array('target' => '/var/clearos/base/daemon/freeswitch.php'),
);

$app['delete_dependency'] = array(
    'app-freeswitch-core',
    'freeswitch',
);
