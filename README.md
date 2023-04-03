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
 
 
