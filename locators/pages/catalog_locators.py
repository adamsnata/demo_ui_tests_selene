filter_button = '//div[@class="filter-button"]'
filter_wrapper = '//aside[@class="CatalogPage__filter-wrapper"]'
collections = '//div[@class="field-type catalog-filter__item"]//*[contains(text(), "{text}")]'
name_of_title = '//span[@class="name__title"]'

product_tags = '//div[@class="SProductCard__tags"]'
product_tags_common = f'{product_tags}//span[@class="tag stringTag"]'
product_tags_accent = f'{product_tags}//span[@class="tag accentTag"]'
tags_checkbox = '//label[@class="s-checkbox selector-checkbox"]'

product_list = '//article[@class="SProductCard product-list__item"]'
