from bottle import route, run, template


@route('/')
def index(name):
    return ('protchargeform', **{'name':name})

@route('/aa/<name>')
def shows_greeting(name):
    return template('index', **{'name':name})

run(host='localhost', port=8000)




def chargeandprop(aa_seq):
    protseq = aa_seq.upper()
    charge = -0.002
    cp = 0
    aa_charge = {"C":-.045,"D":-.999,"E":-.998,"H":.091,
               "K":1,"R":1,"Y":-.001}
     for aa in protseq:
         charge += aa_charge.get(aa,0)
         if aa in aa_charge:
             cp += 1
     prop = float(cp)/len(aa_seq)*100
     return (charge, prop)

 form = cgi.FieldStorage()
 uname = form.getvalue('username','NN')
 seq = form.getvalue('seq', 'QWERTYYTREWQRTYEYTRQWE')
 prop = form.getvalue('prop', 'n')
 jobtitle = form.getvalue('title','No title')
 charge, propvalue = chargeandprop(seq)



 print("<html><body>Job title:{0}<br/>".format(jobtitle))
24 print("Your sequence is:<br/>{0}<br/>".format(seq))
25 print("Net charge: {}<br/>".format(charge))
26 if prop == 'y':
27     print("Proportion of charged AA: {0:.2f}<br/>"
28           .format(propvalue))
29 print("</body></html>")