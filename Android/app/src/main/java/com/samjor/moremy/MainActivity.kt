package com.samjor.moremy

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import com.google.android.material.navigation.NavigationView
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.navigateUp
import androidx.navigation.ui.setupActionBarWithNavController
import androidx.navigation.ui.setupWithNavController
import androidx.drawerlayout.widget.DrawerLayout
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.Toolbar

class MainActivity : AppCompatActivity(),NavigationView.OnNavigationItemSelectedListener  {

    private lateinit var appBarConfiguration: AppBarConfiguration

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val toolbar: Toolbar = findViewById(R.id.toolbar)
        setSupportActionBar(toolbar)

        val fab: FloatingActionButton = findViewById(R.id.fab)

        val drawerLayout: DrawerLayout = findViewById(R.id.drawer_layout)



        val navView: NavigationView = findViewById(R.id.nav_view)
        val navController = findNavController(R.id.nav_host_fragment)


        appBarConfiguration = AppBarConfiguration(setOf(
                R.id.destacado, R.id.busqueda, R.id.cursos,R.id.configuracion), drawerLayout)
        setupActionBarWithNavController(navController, appBarConfiguration)
        navView.setupWithNavController(navController)


        fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                .setAction("Action", null).show()
        }

    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {

        menuInflater.inflate(R.menu.main, menu)
        return true
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        Toast.makeText(this, "SE tocó algo chingada madre", Toast.LENGTH_SHORT).show()
        when (item.itemId) {
            R.id.destacado -> Toast.makeText(this, "Clicó destacado", Toast.LENGTH_SHORT).show()
            R.id.busqueda -> Toast.makeText(this, "Clicó búsqueda", Toast.LENGTH_SHORT).show()
            R.id.cursos -> Toast.makeText(this, "Clicó cursos", Toast.LENGTH_SHORT).show()
            R.id.configuracion -> Toast.makeText(this, "Clicked item four", Toast.LENGTH_SHORT).show()
        }
        return true
    }

    override fun onSupportNavigateUp(): Boolean {
        val navController = findNavController(R.id.nav_host_fragment)
        return navController.navigateUp(appBarConfiguration) || super.onSupportNavigateUp()
    }
}
