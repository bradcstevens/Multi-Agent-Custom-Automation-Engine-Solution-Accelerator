using './macae.bicep'

param resourceSize = {
  o3miniCapacity: 15
  cosmosThroughput: 400
  containerAppSize: {
    cpu: '1.0'
    memory: '2.0Gi'
    minReplicas: 0
    maxReplicas: 1
  }
}
