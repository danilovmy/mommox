# mommox
productcatalog

# HOW TO START
1. git clone
2. Start through docker file
SUPERUSER_EMAIL='test@test.com'
SUPERUSER_PASSWORD='test'
http://127.0.0.1:8000/admin/

or in CLI in repofolder

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000
http://127.0.0.1:8000/admin/


# Task description
Product Catalog

We would like to design an application where all fashion products we know at momox are stored. This catalog should be the single point of reference regarding products in the whole company (for marketing, logistics, marketplaces, pricing, etc.)

The product catalog contains, besides the products, a list of mandatory attributes for every product so that all consumers are aware of which attributes a product must have.
e.g. Shoes might have other attributes than shirts.


# Functional requirements:

Products can be added/changed/removed (through admin panel)
Attributes can be added/changed/removed from products (through admin panel)

Application must provide an interface where consumers can fetch products
(through api)
http://127.0.0.1:8000/products/api/
[{id: 1, owner: 1, template: null, digital: false, visible: true, sorting: 999, title: "My first Product", alt: "first", slug: "product", description: "Test description", attributes: [ ]}]


# Non functional requirements:

Application should be able to deal with more than 10mio products + attributes - i tested it on 5 mlo products, 66mlo properties, around 170 attributes.

Highly available - unclear.

Scalable to 50mio products + attributes - through "django database router" scalability up to 100 mlo. (more not tested)

Changes to products/attributes must be communicated in realtime to consumers - based on cashing system, not on the solution.


# Realising expectation:
Preferred technologies - Python/Django
Reasons for choice: Enough to realize test task.

Visualized high level design: i use lazy python solution for smal/medium miltivendor shops.

Visualized model relationships: products-properties-attributes, product related to owner, Template Product used to setup pattern for choosen product.

Preferred software project architecture and base skeleton with programming languages of your choice: used python & django framework.

Please provide a framework agnostic approach: i have experience to solve Test it in 3 hours. Enough to solve task.
