django-agreements
=================

Arbitrary agreement/lease/terms-and-conditions signing app.

This is used internally at properties.danols.com but feel free to utilise it as a 
skeleton for your needs. If interest dictates code will be transitioned into a stand alone app will

Agreements are accessed by their unique UUID4 number which by its intrinsic nature prevent unauthorised access.
A person must be provided a valid link to view and sign the agreement, for example:

	http://properties.danols.com/leases/0da1c56d-e3da-464c-bc21-717d0f192ee8/