package com.samjor.moremy.ui.configuracion

import androidx.lifecycle.ViewModelProviders
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.samjor.moremy.R

class ConfiguracionFragment : Fragment() {

    companion object {
        fun newInstance() = ConfiguracionFragment()
    }

    private lateinit var viewModel: ConfiguracionViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_configuracion, container, false)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        viewModel = ViewModelProviders.of(this).get(ConfiguracionViewModel::class.java)
        // TODO: Use the ViewModel
    }

}
