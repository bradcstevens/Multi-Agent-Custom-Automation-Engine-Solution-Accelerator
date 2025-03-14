using './macae.bicep'

param resourceSize = {
  o3miniCapacity: 50
  cosmosThroughput: 1000
  containerAppSize: {
    cpu: '2.0'
    memory: '4.0Gi'
    minReplicas: 1
    maxReplicas: 1
  }
}
