package com.samjor.moremy.ui.buscar

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProviders
import com.samjor.moremy.R

class BuscarFragment : Fragment() {

    private lateinit var buscarViewModel: BuscarViewModel

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        buscarViewModel =
                ViewModelProviders.of(this).get(BuscarViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_busqueda, container, false)

        return root
    }
}
