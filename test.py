from lxml import etree

tree_produit=etree.parse("data/dataProduit.xml")
root_produit=tree_produit.getroot()
produits=root_produit.xpath("//produit")

for items in produits:
    entre_xpath=items.xpath("mouvement[@type='Entre' and @date='2025-11-15']/text()")
    sortie_xpath=items.xpath("mouvement[@type='Sortie' and @date='2025-11-15']/text()")
    print(sortie_xpath)