package com.samjor.moremy.ui.destacado

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import com.samjor.moremy.R

class DestacadoFragment : Fragment() {

    private lateinit var destacadoViewModel: DestacadoViewModel

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        destacadoViewModel =
                ViewModelProviders.of(this).get(DestacadoViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_busqueda, container, false)



        return root
    }
}
