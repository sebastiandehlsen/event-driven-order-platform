class OrderCreatedHandler:

    def __call__(
        self,
        payload: dict,
    ) -> None:

        order_id = (
            payload[
                "order_id"
            ]
        )

        print(
            (
                "Received "
                "OrderCreated: "
                f"{order_id}"
            )
        )