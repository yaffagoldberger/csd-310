

  find(student_document_1007, student_document_1008, student_document_1009);
  
Student ID: 1007
First Name: Jamie
Last Name: Minkowitz

Student ID: 1008
First Name: Johnie
Last Name: Gross

Student ID: 1009
First Name: Greenie
Last Name: Sturm


  result = db.collection.update_one({“student_id”: 1007}, {“$set”: {“last_name”: “Varenberg”}});
  
  find(student_document_1007);
  
Student ID: 1007
First Name: Jamie
Last Name: Varenberg

  
  
