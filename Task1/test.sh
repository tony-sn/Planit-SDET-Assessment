file_list=("001_Navigate_Shop_Page" "002_Buy_Shop_Page" "003_Click_Login_Link" "004_Navigate_Cart_Page" "005_Edit_Item_Cart_Page" "006_Empty_Cart" "007_Navigate_Checkout_Page" "008_Form_Checkout_Page" "009_Navigate_Contact_Page" "010_Form_Contact_Page")

for py_file in "${file_list[@]}"
do
    python3 ${py_file}/test*.py
done

