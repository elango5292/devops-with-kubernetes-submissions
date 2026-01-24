## Exercise: 3.9. DBaaS vs DIY

### DBaaS (Database as a Service)

Database as a Service (DBaaS) is a product offering where the provider manages a database on its own infrastructure, stripping away the complexity of provisioning, deploying, maintaining, and scaling. The database is usually open-source, but can also be a provider's proprietary database, which the user's application accesses using APIs or SDKs.

#### Pros:
- Since DBaaS abstracts away the complexity of hosting a database, it is highly preferred for small teams who may not be able to manage their own database infrastructure.
- Although more costly than self-managed options in terms of the raw cloud bill, it is often cheaper when considering the Total Cost of Ownership (TCO), as self-managing requires human resources which ends up costing more.
- The providers usually have SLAs which guarantee the reliability and availability of the database.
- The security and updates of database versions are managed by the provider itself; hence, rolling database patches are automatic.
- Best practices, such as backups, can be managed easily with the click of a button.

#### Cons:
- DBaaS is expensive at a large scale and costs more for resources like storage and compute than it would in a self-managed infrastructure.
- Customizations are limited, as the DB versions are managed by the providers; usually, only they have the access to support different DB versions or extensions.
- As the infrastructure is not inside the cluster, the privacy and security implementation is not visible to the user and often involves trust in the provider.
- The users have the responsibility to manage access credentials. As the DB is outside the cluster, credentials need to be stored and provided safely to the user's application.

---

### DIY (Do It Yourself)

DIY involves the user self-provisioning and managing the database infrastructure, usually using Kubernetes StatefulSets and PersistentVolumes. The users are responsible for deploying, managing, maintaining, and scaling the database.

#### Pros:
- Cheaper in terms of the raw cloud bill, which is helpful for small apps or prototyping.
- Users have the utmost freedom to choose any alternative, special versions, or plugins for the database if it provides a specific feature they want.

#### Cons:
- We need to manage and set up everything ourselves, which usually requires a slightly larger engineering team.
- High operational complexity; if something breaks, the team is responsible for fixing it rather than the provider.
