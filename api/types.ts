export enum DeploymentEnvironment {
  PRODUCTION = 'production',
  STAGING = 'staging',
  DEVELOPMENT = 'development',
  TEST = 'test',
}

export enum ArtifactType {
  CONTAINER_IMAGE = 'container-image',
  DOCKER_IMAGE = 'docker-image',
  ECR_IMAGE = 'ecr-image',
  ARTIFACT = 'artifact',
}

export enum DockerComposeFile {
  DOCKER_COMPOSE_FILE = 'docker-compose.yml',
}

export enum AWSRegion {
  US_WEST_2 = 'us-west-2',
  US_EAST_1 = 'us-east-1',
  US_EAST_2 = 'us-east-2',
  EU_WEST_1 = 'eu-west-1',
  EU_WEST_2 = 'eu-west-2',
  EU_CENTRAL_1 = 'eu-central-1',
}

export enum IacEngine {
  TERRAFORM = 'terraform',
  CLOUDFORMATION = 'cloudformation',
  KUBEINFRASTRUCTURE = 'kubeinfrastructure',
}