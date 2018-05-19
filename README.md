[DEPRECATED]
There is already the [quickstart](https://hub.docker.com/r/stellar/quickstart/) image that ships with PostgreSQL and the Horizon server.
Since I don't need to run multiple stellar-core tasks in the docker stack, I decided to use that image instead.
The new repository can be found [here](https://github.com/matheusb-comp/stellar-docker).

Docker stack configuration to run a stellar-core node, with a simple Django appplication to serve data from the core DB.
