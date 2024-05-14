import mysql.connector 
import streamlit as st
import google.generativeai as genai
import pandas as pd

genai.configure(api_key="AIzaSyD5GNawVGUZ7OLckYn-JT1d2YtCbxaqKbI")

mydb = mysql.connector.connect(
    host="localhost",
    database="fssservicedb",
    user="root",
    password="toor#123"
)

prompt=[
    """
    You are an expert in converting English question to SQL query!
    The SQL database has the name fssservicedb and has the following tables - Table:enquiries
    Table:quotation_charges
    Table:quotation_documents
    Table:quotation_histories
    Table:quotation_history_charges
    Table:quotation_history_documents
    Table:quotation_term_condition_mapping
    Table:quotations
    Table:ship_activity_documents
    Table:shiplines
    Table:shipment_activities
    Table:shipment_charges
    Table:shipment_charges_documents
    Table:shipment_documents
    Table:shipment_notifications
    Table:shipments
    Table:invoice_lineitems
    Table:invoice_payments
    Table:invoices
    Below are there respective columns 

    Table:enquiries

    Columns:
    enquiry_id
    int AI PK
    enquiry_number
    varchar(50)
    emp_id
    int
    cust_id
    int
    customer_address
    int
    comp_id
    int
    branch
    int
    mode_of_transfer
    enum('AIR','SEA','ROAD','RAIL','OTHER')
    sea_shipment_id
    int
    air_shipment_id
    int
    type_of_transaction
    enum('I','E','B')
    shipper_cust_id
    int
    shipper_address
    int
    consignee_cust_id
    int
    sales_executive
    int
    consignee_address
    int
    notifying_cust_id
    int
    notifying_cust_address
    int
    notifying_party
    int
    incoterms
    enum('EXW','FCA','FAS','FOB','CFR','CIF','CIP','CPT','DAF','DES','DEQ','DDU','DDP','DAT','DAP')
    goods_description
    varchar(500)
    HSCODE
    varchar(100)
    enquiry_date
    datetime
    freight
    enum('C','P')
    payable_at
    varchar(100)
    dispatch_at
    varchar(100)
    enquiry_status
    enum('INCOMPLETE','COMPLETE','PENDING')
    place_of_pick_up
    varchar(500)
    place_of_delivery
    varchar(500)
    service_type_id
    int
    internal_remarks
    varchar(500)
    remarks
    varchar(500)
    is_deleted
    tinyint(1)
    created_by
    int
    created_at
    datetime
    updated_by
    int
    updated_at
    datetime
    from_cust_portal
    tinyint(1)
    is_hazardous
    tinyint(1)






















    Table:quotation_charges

    Columns:
    quotation_charge_id
    int AI PK
    quote_id
    int
    charge_id
    int
    charge_type_id
    int
    vendor
    int
    vendor_ref_no
    varchar(100)
    vendor_ref_date
    datetime
    unit_id
    int
    quantity
    double(16,5)
    buy_currency
    int
    buy_cost
    double(16,5)
    buy_exchange_rate
    double(16,5)
    buy_cost_base_ccy
    double(16,5)
    buy_tax
    int
    buy_tax_amount
    double(16,5)
    buy_total_cost
    double(16,5)
    buy_fcy_amount
    double(16,5)
    buy_amount
    double(16,5)
    sale_currency
    int
    sale_cost
    double(16,5)
    sale_exchange_rate
    double(16,5)
    sale_cost_base_ccy
    double(16,5)
    sale_tax
    int
    sale_tax_amount
    double(16,5)
    sale_total_cost
    double(16,5)
    sale_fcy_amount
    double(16,5)
    sale_amount
    double(16,5)
    margin
    double(16,5)
    margin_amount
    double(16,5)
    profit
    double(16,5)
    is_deleted
    tinyint(1)





    Table:quotation_documents

    Columns:
    quotation_document_id
    int AI PK
    name
    varchar(200)
    ref_no
    varchar(100)
    ref_date
    datetime
    upload_date
    datetime
    file_path
    varchar(200)
    quote_id
    int
    comp_id
    int
    branch
    int
    is_deleted
    tinyint(1)








    Table:quotation_histories

    Columns:
    quote_id
    int AI PK
    quote_number
    varchar(50)
    version
    int
    emp_id
    int
    enquiry_id
    int
    enquiry_number
    varchar(50)
    quote_date
    datetime
    validity
    int
    quote_status
    enum('P','R','C','A','I','PP','RR','RV')
    reason
    varchar(500)
    enquiry_date
    datetime
    enquiry_status
    enum('INCOMPLETE','COMPLETE','PENDING')
    is_deleted
    tinyint(1)
    created_by
    int
    created_at
    datetime
    updated_by
    int
    updated_at
    datetime
    cust_id
    int
    customer_address
    int
    comp_id
    int
    branch
    int
    mode_of_transfer
    enum('AIR','SEA','ROAD','RAIL','OTHER')
    sea_shipment_id
    int
    air_shipment_id
    int
    type_of_transaction
    enum('I','E','B')
    shipper_cust_id
    int
    shipper_address
    int
    consignee_cust_id
    int
    consignee_address
    int
    sales_executive
    int
    notifying_cust_id
    int
    notifying_cust_address
    int
    notifying_party
    int
    incoterms
    enum('EXW','FCA','FAS','FOB','CFR','CIF','CIP','CPT','DAF','DES','DEQ','DDU','DDP','DAT','DAP')
    goods_description
    varchar(500)
    HSCODE
    varchar(100)
    freight
    enum('C','P')
    payable_at
    varchar(100)
    dispatch_at
    varchar(100)
    place_of_pick_up
    varchar(500)
    place_of_delivery
    varchar(500)
    service_type_id
    int
    internal_remarks
    varchar(500)
    remarks
    varchar(500)
    terms_description
    varchar(2000)
    total_buy_cost
    double(16,5)
    total_sale_cost
    double(16,5)
    total_margin
    double(16,5)





    Table:quotation_history_charges

    Columns:
    quotation_charge_id
    int AI PK
    quote_id
    int
    charge_id
    int
    charge_type_id
    int
    vendor
    int
    vendor_ref_no
    varchar(100)
    vendor_ref_date
    datetime
    unit_id
    int
    quantity
    double(10,2)
    buy_currency
    int
    buy_cost
    double(16,5)
    buy_exchange_rate
    double(10,2)
    buy_cost_base_ccy
    double(16,5)
    buy_tax
    int
    buy_tax_amount
    double(16,5)
    buy_total_cost
    double(16,5)
    buy_fcy_amount
    double(16,5)
    buy_amount
    double(16,5)
    sale_currency
    int
    sale_cost
    double(16,5)
    sale_exchange_rate
    double(10,2)
    sale_cost_base_ccy
    double(16,5)
    sale_tax
    int
    sale_tax_amount
    double(16,5)
    sale_total_cost
    double(16,5)
    sale_fcy_amount
    double(16,5)
    sale_amount
    double(16,5)
    margin
    double(10,2)
    margin_amount
    double(16,5)
    profit
    double(16,5)
    is_deleted
    tinyint(1)






    Table:quotation_history_documents

    Columns:
    quotation_document_id
    int AI PK
    name
    varchar(200)
    ref_no
    varchar(100)
    ref_date
    datetime
    upload_date
    datetime
    file_path
    varchar(200)
    quote_id
    int
    comp_id
    int
    branch
    int
    is_deleted
    tinyint(1)







    Table:quotation_term_condition_mapping

    Columns:
    quotation_term_condition_mapping_id
    int AI PK
    quote_id
    int
    term_conditions_id
    int






    Table:quotations

    Columns:
    quote_id
    int AI PK
    quote_number
    varchar(50)
    version
    int
    emp_id
    int
    enquiry_id
    int
    enquiry_number
    varchar(50)
    quote_date
    datetime
    validity
    int
    quote_status
    enum('P','R','C','A','I','PP','RR','RV','RRD')
    reason
    varchar(500)
    enquiry_date
    datetime
    enquiry_status
    enum('INCOMPLETE','COMPLETE','PENDING')
    cust_id
    int
    customer_address
    int
    comp_id
    int
    branch
    int
    mode_of_transfer
    enum('AIR','SEA','ROAD','RAIL','OTHER')
    sea_shipment_id
    int
    air_shipment_id
    int
    type_of_transaction
    enum('I','E','B')
    shipper_cust_id
    int
    shipper_address
    int
    consignee_cust_id
    int
    consignee_address
    int
    sales_executive
    int
    notifying_cust_id
    int
    notifying_cust_address
    int
    notifying_party
    int
    incoterms
    enum('EXW','FCA','FAS','FOB','CFR','CIF','CIP','CPT','DAF','DES','DEQ','DDU','DDP','DAT','DAP')
    goods_description
    varchar(500)
    HSCODE
    varchar(100)
    freight
    enum('C','P')
    payable_at
    varchar(100)
    dispatch_at
    varchar(100)
    place_of_pick_up
    varchar(500)
    place_of_delivery
    varchar(500)
    service_type_id
    int
    internal_remarks
    varchar(500)
    remarks
    varchar(500)
    terms_description
    varchar(2000)
    total_buy_cost
    double(16,5)
    total_sale_cost
    double(16,5)
    total_margin
    double(16,5)
    transit_days
    int
    is_deleted
    tinyint(1)
    created_by
    int
    created_at
    datetime
    updated_by
    int
    updated_at
    datetime
    sent_email_already
    tinyint(1)
    status_from_cust_portal
    tinyint(1)











    Table:ship_activity_documents

    Columns:
    activity_document_id
    int AI PK
    name
    varchar(200)
    ref_no
    varchar(100)
    ref_date
    datetime
    upload_date
    datetime
    file_path
    varchar(200)
    shipment_activity_id
    int
    comp_id
    int
    branch
    int
    is_deleted
    tinyint(1)





    Table:shiplines

    Columns:
    ship_line_id
    int AI PK
    name
    varchar(100)
    SCAC
    varchar(50)
    website
    varchar(100)
    comp_id
    int
    is_deleted
    tinyint(1)
    created_by
    int
    created_at
    datetime
    updated_by
    int
    updated_at
    datetime
    tracking_website
    varchar(200)








    Table:shipment_activities

    Columns:
    shipment_activity_id
    int AI PK
    shipment_id
    int
    comp_id
    int
    branch
    int
    activity_name
    varchar(100)
    activity_status
    enum('PLANNED','INPROGRESS','DONE')
    planned_date
    datetime
    actual_date
    datetime
    remark
    varchar(500)
    is_deleted
    tinyint(1)






    Table:shipment_charges

    Columns:
    shipment_charge_id
    int AI PK
    shipment_id
    int
    charge_id
    int
    charge_type_id
    int
    vendor
    int
    vendor_ref_no
    varchar(100)
    vendor_ref_date
    datetime
    unit_id
    int
    quantity
    double(16,5)
    buy_currency
    int
    buy_cost
    double(16,5)
    buy_exchange_rate
    double(16,5)
    buy_cost_base_ccy
    double(16,5)
    buy_tax
    int
    buy_tax_amount
    double(16,5)
    buy_total_cost
    double(16,5)
    buy_fcy_amount
    double(16,5)
    buy_amount
    double(16,5)
    sale_currency
    int
    sale_cost
    double(16,5)
    sale_exchange_rate
    double(16,5)
    sale_cost_base_ccy
    double(16,5)
    sale_tax
    int
    sale_tax_amount
    double(16,5)
    sale_total_cost
    double(16,5)
    sale_fcy_amount
    double(16,5)
    sale_amount
    double(16,5)
    margin
    double(16,5)
    margin_amount
    double(16,5)
    profit
    double(16,5)
    sales_invoice
    tinyint(1)
    purchase_invoice
    tinyint(1)
    is_deleted
    tinyint(1)






    Table:shipment_charges_documents

    Columns:
    shipment_charge_doc_id
    int AI PK
    shipment_charge_id
    int
    reference_no
    varchar(100)
    reference_date
    datetime
    date
    datetime
    path
    varchar(100)
    is_deleted
    tinyint(1)



    Table:shipment_documents

    Columns:
    shipment_document_id
    int AI PK
    name
    varchar(200)
    ref_no
    varchar(100)
    ref_date
    datetime
    upload_date
    datetime
    file_path
    varchar(200)
    shipment_id
    int
    comp_id
    int
    branch
    int
    is_deleted
    tinyint(1)






    Table:shipment_notifications

    Columns:
    tracking_id
    int AI PK
    shipment_id
    int
    mode_of_transfer
    enum('SEA','AIR')
    type
    int
    order_no
    varchar(255)
    tracking_no
    varchar(255)
    comp_id
    int
    branch_id
    int
    customer_id
    int







    Table:shipments

    Columns:
    shipment_id
    int AI PK
    shipment_number
    varchar(50)
    emp_id
    int
    enquiry_id
    int
    enquiry_number
    varchar(50)
    quote_id
    int
    quotation_number
    varchar(50)
    air_shipment_id
    int
    sea_shipment_id
    int
    vessel_id
    int
    airline_id
    int
    flight_name
    varchar(50)
    flight_no
    varchar(50)
    hawb_no
    varchar(50)
    hawb_date
    datetime
    mawb_date
    datetime
    mawb_no
    varchar(50)
    vessel_name
    varchar(50)
    voyage_no
    varchar(50)
    carrier_id
    int
    hbl_no
    varchar(50)
    hbl_date
    datetime
    mbl_no
    varchar(50)
    mbl_date
    datetime
    origin_agent
    int
    delivery_agent
    int
    bl_place_of_issue
    varchar(200)
    no_of_original_bl
    varchar(50)
    exim_flag
    varchar(50)
    do_no
    varchar(50)
    do_date
    datetime
    cutoff_date
    datetime
    marks_no
    varchar(50)
    internal_remarks
    varchar(500)
    remarks
    varchar(500)
    boe_no
    varchar(50)
    carrier_booking_no
    varchar(50)
    carrier_booking_date
    datetime
    document_cutoff_date
    datetime
    document_ref_no
    varchar(50)
    port_cutoff_date
    datetime
    aes_filing_date
    datetime
    first_receiving_date
    datetime
    ams_ref_no
    varchar(50)
    can_sent_date
    datetime
    accounting_information
    varchar(200)
    handling_information
    varchar(200)
    manifest_consignee_address
    varchar(500)
    manifest_shipper_address
    varchar(500)
    on_board_date
    datetime
    scn_no
    varchar(20)
    vessel_code
    varchar(50)
    isf_no
    varchar(50)
    it_no
    varchar(50)
    it_date
    datetime
    it_city
    varchar(50)
    it_destination
    varchar(50)
    switch_bl_ref_no
    varchar(50)
    barcode_value
    varchar(50)
    barcode_value_date
    datetime
    declaration_no
    varchar(50)
    declaration_date
    datetime
    claim_no
    varchar(50)
    claim_date
    datetime
    last_free_date
    datetime
    go_date
    datetime
    pickup_ref_no
    varchar(50)
    delivery_mode
    varchar(50)
    load_ref_no
    varchar(50)
    bl_no_of_copies
    int
    shipper_ref_no
    varchar(100)
    shipper_ref_date
    datetime
    shipment_status
    enum('I','C','CR','B','P','DTW','DTCFS','DTT','DTP','L','S','UL','DTC')
    shipment_date
    datetime
    shipment_closing_date
    datetime
    quote_date
    datetime
    validity
    int
    quote_status
    enum('P','R','C','A','I')
    reason
    varchar(500)
    cust_id
    int
    customer_address
    int
    comp_id
    int
    branch
    int
    mode_of_transfer
    enum('AIR','SEA','ROAD','RAIL','OTHER')
    type_of_transaction
    enum('I','E','B')
    shipper_cust_id
    int
    shipper_address
    int
    consignee_cust_id
    int
    consignee_address
    int
    sales_executive
    int
    notifying_cust_id
    int
    notifying_cust_address
    int
    notifying_party
    int
    incoterms
    enum('EXW','FCA','FAS','FOB','CFR','CIF','CIP','CPT','DAF','DES','DEQ','DDU','DDP','DAT','DAP')
    goods_description
    varchar(500)
    HSCODE
    varchar(50)
    enquiry_date
    datetime
    freight
    enum('C','P')
    payable_at
    varchar(100)
    dispatch_at
    varchar(100)
    place_of_pick_up
    varchar(500)
    place_of_delivery
    varchar(500)
    service_type_id
    int
    enquiry_status
    enum('INCOMPLETE','COMPLETE','PENDING')
    total_buy_cost
    double(16,5)
    total_sale_cost
    double(16,5)
    total_margin
    double(16,5)
    pickup_transporter
    varchar(200)
    pickup_ref_date
    datetime
    pickup_vehicle_details
    varchar(100)
    pickup_driver_name
    varchar(100)
    pickup_driver_no
    varchar(50)
    pickup_driver_lic_no
    varchar(50)
    pickup_date
    datetime
    offload_date
    datetime
    fumigation
    varchar(100)
    fumigation_certificate_no
    varchar(50)
    fumigation_date
    datetime
    custom_clr_exp_cha_name
    varchar(100)
    shipping_bill_no
    varchar(50)
    shipping_bill_date
    datetime
    carting_date
    datetime
    egm_no
    varchar(50)
    egm_date
    datetime
    post_ship_docs_dispatch
    tinyint(1)
    doc_dispatch_place
    varchar(100)
    doc_dispatch_date
    datetime
    doc_disp_courier_details
    varchar(100)
    igm_no
    varchar(50)
    igm_date
    datetime
    flight_date
    datetime
    rotation_no
    varchar(50)
    cargo_arrival_handover
    tinyint(1)
    cargo_arrival_handover_date
    datetime
    custom_clr_imp_cha_name
    varchar(100)
    boe_date
    datetime
    delivery_transporter
    varchar(200)
    delivery_ref_no
    varchar(50)
    delivery_ref_date
    datetime
    delivery_vehicle_details
    varchar(100)
    delivery_driver_name
    varchar(100)
    delivery_driver_no
    varchar(50)
    delivery_driver_lic_no
    varchar(50)
    delivery_date
    datetime
    carting_point
    varchar(500)
    sales_invoice
    tinyint(1)
    purchase_invoice
    tinyint(1)
    is_deleted
    tinyint(1)
    created_by
    int
    created_at
    datetime
    updated_by
    int
    updated_at
    datetime
    is_registered
    int
    carrier_code
    varchar(100)
    order_no
    varchar(100)
    is_registered_bn
    int
    is_registered_cn
    int
    is_registered_bl
    int
    order_no_bn
    varchar(100)
    order_no_cn
    varchar(100)
    booking_number
    varchar(100)
    container_number
    varchar(100)
    order_no_bl
    varchar(100)













    Table:invoice_lineitems

    Columns:
    invoice_item_id
    int AI PK
    invoice_id
    int
    shipment_charge_id
    int
    line_item
    int
    line_item_type_id
    int
    vendor
    int
    vendor_ref_no
    varchar(100)
    vendor_ref_date
    datetime
    quantity
    double(16,5)
    item_currency_id
    int
    item_cost
    double(16,5)
    item_exchange_rate
    double(16,5)
    item_cost_base_ccy
    double(16,5)
    item_tax_id
    int
    item_tax_amount
    double(16,5)
    item_total_cost
    double(16,5)
    item_fcy_amount
    double(16,5)
    item_amount
    double(16,5)
    item_billing_amount
    double(16,5)
    goods_service
    enum('GOODS','SERVICE')
    description
    varchar(500)
    sac_code
    varchar(50)
    hsn_code
    varchar(50)
    account_id
    int
    is_deleted
    tinyint(1)






    Table:invoice_payments

    Columns:
    invoice_payment_id
    int AI PK
    inv_payment_number
    varchar(50)
    inv_id
    int
    comp_id
    int
    branch
    int
    received_amount
    double(16,5)
    received_account
    int
    payment_received_number
    varchar(50)
    ref_number_1
    varchar(50)
    ref_date_1
    datetime
    ref_number_2
    varchar(50)
    ref_date_2
    varchar(50)
    billing_currency
    int
    exchange_rate
    double(16,5)
    total_amount
    double(16,5)
    sale_tds_amount
    double(16,5)
    status
    enum('GENERATED','APPROVED','POSTED','REJECTED')
    inv_type
    enum('SALES','PURCHASE','CREDIT_NOTE','DEBIT_NOTE')
    inv_payment_date
    datetime
    reject_reason
    varchar(500)
    is_deleted
    tinyint(1)






    Table:invoices

    Columns:
    inv_id
    int AI PK
    inv_number
    varchar(50)
    inv_ref_id
    int
    inv_ref_number
    varchar(50)
    inv_ref_date
    datetime
    debit_note_ref_number
    varchar(50)
    debit_note_ref_date
    datetime
    inv_date
    datetime
    inv_type
    enum('SALES','PURCHASE','CREDIT_NOTE','DEBIT_NOTE')
    cust_id
    int
    cust_address_id
    int
    cust_po_no
    varchar(100)
    cust_po_date
    datetime
    comp_id
    int
    branch
    int
    job_id
    int
    job_number
    varchar(50)
    shipment_id
    int
    shipment_number
    varchar(50)
    inv_currency
    int
    inv_status
    enum('GENERATED','APPROVED','POSTED','REJECTED')
    payment_status
    enum('P','UP','PP')
    inv_tax_amount
    double(16,5)
    inv_amount
    double(16,5)
    billing_amount
    double(16,5)
    paid_amount
    double(16,5)
    outstanding_amount
    double(16,5)
    inv_exchange_rate
    double(16,5)
    general_ledger_date
    datetime
    remark
    varchar(500)
    reject_reason
    varchar(500)
    tds_percentage
    int
    tds_amount
    double(16,5)
    vendor
    int
    vendor_tds_id
    int
    due_date
    datetime
    is_deleted
    tinyint(1)


    \n\nFor example,\nExample 1 - Retrieve the enquiry status of xyz enquiry number, 
        the SQL command will be something like this SELECT enquiry_status
    FROM enquiries
    WHERE enquiry_number = 'your_enquiry_number';

    \nExample 2 - Retrieve all shipments with a specific sales executive as the notifying party
    , 
        the SQL command will be something like this SELECT 
        s.*
    FROM 
        shipments s
    JOIN 
        enquiries e ON s.enquiry_id = e.enquiry_id
    WHERE 
        e.sales_executive = '156';

    \nExample 3 -  get the enquiry status ,shipment id, and buying cost of 'IVBRPN21000000001' ivn number
    , 
        the SQL command will be something like thisSELECT 
        e.enquiry_status,
        s.shipment_id,
        qc.buy_cost AS buying_cost
    FROM 
        invoices inv
    JOIN 
        shipment_charges qc ON inv.shipment_id = qc.shipment_id
    JOIN 
        shipments s ON qc.shipment_id = s.shipment_id
    JOIN 
        quotations q ON s.quote_id = q.quote_id
    JOIN 
        enquiries e ON q.enquiry_id = e.enquiry_id
    WHERE 
        inv.inv_number = 'your_invoice_number';

    \nExample 4 -   What are the documents associated with a specific shipment?
    , 
        the SQL command will be something like SELECT sd.*
    FROM shipment_documents sd
    JOIN shipments s ON sd.shipment_id = s.shipment_id
    WHERE s.shipment_number = 'your_shipment_number';

        also the sql code should not have ``` in beginning or end and sql word in output

    """
]
model = genai.GenerativeModel('gemini-pro')
#Function to load the goole gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

#streamlit app
st.set_page_config(
   page_title="RAG",
   layout="wide")
st.title("SQL Agent for data Retrival")

#question = st.text_input("Input: ", key="input")

# check for messages in session and create if not exists
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there, am ChatGPT clone"}
    ]

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)


mycursor = mydb.cursor()

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = get_gemini_response(user_prompt,prompt)
            result=mycursor.execute(ai_response)
            response = mycursor.fetchall()
            for row in response:
                st.write(row)
    new_ai_message = {"role": "assistant", "content": row}
    st.session_state.messages.append(new_ai_message)

