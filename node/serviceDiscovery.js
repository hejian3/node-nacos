'use strict';

const NacosNamingClient = require('nacos').NacosNamingClient;
const sleep = require('mz-modules/sleep');
const logger = console;

async function test() {
  const client = new NacosNamingClient({
    logger,
    serverList: '127.0.0.1:8848',
    namespace: 'public',
  });
  await client.ready();

  const serviceName = 'nodejs';

  // console.log();
  // console.log('before', await client.getAllInstances(serviceName, ['NODEJS']));
  // console.log();

  client.subscribe(serviceName, hosts => {
    console.log(hosts);
  });

  await client.registerInstance(serviceName, {
    ip: '127.0.0.1',
    port: 8080,
  });
  await client.registerInstance(serviceName, {
    ip: '127.0.0.1',
    port: 8080,
  });

  // const hosts = await client.getAllInstances(serviceName);
  // console.log();
  // console.log(hosts);
  // console.log();

  await sleep(5000);

  await client.deregisterInstance(serviceName, {
    ip: '1.1.1.1',
    port: 8080,
  });
}

test().catch(err => {
  console.log(err);
});