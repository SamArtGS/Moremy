package com.samjor.moremy.ui.curso

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import com.samjor.moremy.R

class CursoFragment : Fragment() {

    private lateinit var cursoViewModel: CursoViewModel

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        cursoViewModel =
                ViewModelProviders.of(this).get(CursoViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_cursos, container, false)
        val textView: TextView = root.findViewById(R.id.text_slideshow)
        cursoViewModel.text.observe(viewLifecycleOwner, Observer {
            textView.text = it
        })
        return root
    }
}
