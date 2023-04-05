# MovingLake Custom Connector Tempaltes
Templates of the files needed to configure a new custom connector within MovingLake.

# connector.json

This JSON configures the authentication, defaults and other properties of the connector. Here is a list of keys and their meaning:
* code: The unique code name for this connector. Can't clash with any other connector code name in the public namespace or in your organization's private namespace.
* name: A human friendly name to refer to it.
* description: A friendly description of the connector.
* scheme_form_cred: Dictionary detailing what the configuration / authentication form should consist of, and how it should be rendered.
  * layout: Bootstrap information on how the fields should be rendered
  * schema_form: Content and configuration of each field.
* provider_json: Configuration defaults and authentication for the API at hand.
  * auth: Details which authentication to be used important for out of the box authentication methods.
  * defaults: Default fields to use when calling the API. Please check the entity configuration to see all possible fields.
  * promote_creds_to_params: If any value within the authentication / configuration form will be used to call the API, make them available.
  * url_root: The domain of the API in the form of https://subdomains.domain.com
  * url_sandbox: Optionally, the domain of the staging or sandbox enviroment of the API.
* category_connector: The categories to which this connector belongs to. See the table below for all Categories.
* icon: The name of the icon. Should be in the form of s3/myiconname.png. Can be jpg, png or webp
* is_user_authentication: Reserved for more complicated authentication flows. Normally false.

### Connector Categories

| Category ID | Category Name |
| ----------- | ------------- |
| Default    | 1 |
| Ecommerce  | 2 |
| KYC        | 3 |
| HelpDesk   | 4 |
| FinTech    | 5 |
| Hospitality| 6 |
| Utilities  | 7 |
| Insurance  | 8 |
| Creators   | 9 |
| Construction| 10 |
| Trading    | 11 |
| Banks      | 12 |
| Digital wallets| 13 |
| Blockchain| 14 |
| Government| 15 |
| Services| 16 |
| Datastores| 17 |
| Marketing| 18 |
| PMS| 19 |
| Communication| 20 |

 # entities.json

This json file contains the configuration for each endpoint of an API (called entity henceforth). Note that one entity gets transformed into potentially multiple tables in your SQL destination.

## name
- Type: string
- Description: The name of the entity, used to identify the data being returned. Destination table names will use this field to name the tables.

## description
- Type: string
- Description: A brief description of the data returned by the entity.

## entity_json
- Type: object
- Description: Contains the configuration and details of the entity.

### key
- Type: array of strings
- Description: The primary key(s) used to uniquely identify records in the entity.

### endpoint
- Type: string
- Description: The API endpoint to be used to fetch the data for this entity. Must start with a slash and not include any query strings or domain related characters e.g "/api/v1/orders"

### json_node
- Type: string
- Description: The JSON path to extract the relevant data from the API response. Say we have a response from an orders endpoint, the json_node should reflect the json path to obtain the orders. The data extracted will be only what's in this json_node path. If the entire JSON is what will be inserted in the destination then use ".".

### description
- Type: string
- Description: A brief description of the data returned by the entity.

### every_record
- Type: object
- Description: Designates dependencies for this entity.

#### name
- Type: string
- Description: The name of the parent entity.

#### type
- Type: string
- Description: The type of processing to be applied to each record. Normally "one-by-one" but we support also "comma-delimited".

#### params
- Type: string | array of strings
- Description: The parameter(s) to be passed while processing each record.

#### add_to_payload
- Type: boolean
- Description: Indicates whether the parent field should be added to the payload.

### has_paginate
- Type: boolean
- Description: Indicates whether the API supports pagination or not.

### key_name_page
- Type: string
- Description: The parameter name to be used for pagination.

### json_node_page
- Type: string
- Description: The JSON path to extract the pagination token from the API response.

### query_params
- Type: object
- Description: A set of key-value pairs to be sent as query parameters with the API request.

### has_token_page
- Type: boolean
- Description: Indicates whether the API uses a token for pagination or not.

### date_format
- Type: string
- Description: The format used for date values.

### key_end_date
- Type: string
- Description: The parameter name to be used for the end date.

### key_start_date
- Type: string
- Description: The parameter name to be used for the start date.

### key_name_limit
- Type: string
- Description: The parameter name to be used for the maximum number of records per page.

### filter_by_dates
- Type: boolean
- Description: Indicates whether the API should filter data based on date ranges.

### return_rows
- Type: integer
- Description: The number of rows to be returned in the result.

### ignore_dedup
- Type: boolean
- Description: Indicates whether deduplication should be ignored or not.

### skip_write
- Type: boolean
- Description: Indicates whether this entity should not be sent to the destination. Normally here for parent entities which shouldn't be reflected on the destination.

### deprecated
- Type: boolean
- Description: Indicates whether the entity is deprecated or not.

### method
- Type: string
- Description: The HTTP method used for the API request (e.g., GET, POST).

## repeat_every
- Type: integer
- Description: The frequency (in seconds) at which the data fetching should be repeated.

## is_active
- Type: boolean
- Description: Indicates whether the configuration is active or not.

## timing_configuration
- Type: object
- Description: Contains the timing configuration details.

### validation_data
- Type: object
- Description: Contains data used for validating the timing configuration.

#### default_value
- Type: integer
- Description: The default value for the `repeat_every` setting (in seconds).

#### allowed_repeat_every
- Type: array of objects
- Description: A list of allowed `repeat_every` values with their corresponding labels.

##### seconds
- Type: integer
- Description: The number of seconds for the `repeat_every` option.

##### label
- Type: string
- Description: The label used to represent the `repeat_every` option in the UI.

### strategy
- Type: string
- Description: The strategy used for scheduling data fetching (e.g., `repeat_every`).

## uses_cron_expression
- Type: boolean
- Description: Indicates whether a cron expression is used for scheduling data fetching.
