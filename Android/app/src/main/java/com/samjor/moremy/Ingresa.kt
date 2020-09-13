package com.samjor.moremy

import android.app.ProgressDialog
import android.content.Intent
import android.os.Bundle
import android.text.TextUtils
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_ingresa.*

class Ingresa : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_ingresa)


        botonRegistro.setOnClickListener{
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
        botonOlvidoContrasena.setOnClickListener{
            val intent = Intent(this,MainActivity::class.java)
            startActivity(intent)
        }

        botonIngreso.setOnClickListener {
            ingresar()
            //val intent = Intent(this,MainActivity::class.java)
            //startActivity(intent)
        }
    }


    fun ingresar(){
        var progressBar = ProgressDialog(this)
        val email = correoIngresa.text.toString()
        val password = contrasenaIngresa.text.toString()
        if (!TextUtils.isEmpty(email) && !TextUtils.isEmpty(password)) {
            progressBar.setMessage("Iniciando sesión")
            progressBar.show()
            //Iniciamos sesión con el método signIn y enviamos usuario y contraseña
            val intent = Intent(this,MainActivity::class.java)
            startActivity(intent)
            progressBar.hide()
        } else {
            //En caso que el usuario no haya ingresado todos los campos
            Toast.makeText(this, "No has capturado todos los campos", Toast.LENGTH_SHORT).show()
        }
    }

}